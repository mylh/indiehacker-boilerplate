import _ from 'underscore';
import React from 'react';
import Alert from 'react-bootstrap/Alert';
import Form from 'react-bootstrap/Form';
import { PayPalScriptProvider, PayPalButtons } from '@paypal/react-paypal-js';

import { Utils } from './utils';
import api from './api';


export default class CreateSessionController extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            // general interface
            alert: [],
            canEditForm: true,
            canPay: false,


            // data
            orderId: null,
            email: '',
            emailValid: false,
            newsletter: true,
            addon: false,

            // price
            price: 0,
            tax: 0,
            total_price: 0,

        };
        Utils.autoBindClass(this);
    }

    componentDidMount() {
        this.updatePrice();
    }


    apiErrorHandler(error) {
        var userMsg = 'Error creating a new order: ';
        if (error.response) {
            console.log(error.response);
            if (error.response.data && error.response.data.message) {
                userMsg += error.response.data.message;
            }
        } else if (error.request) {
            // The request was made but no response was received
            userMsg += 'Your request could not be processed at the moment. Try back later';
            console.log(error.request);
        } else if (error.message) {
            userMsg += error.message || error.toString();
        }
        userMsg += ' Please try again later or contact support';
        console.log(error);

        this.setState({
            alert: [userMsg],
        });
    }

    validateOrder() {
        if (!this.state.emailValid) {
            this.setState({ alert: ['Please enter valid email address'] });
            return false;
        }

        return true;
    }

    handleCreateOrder(e) {
        e.preventDefault();
        if (!this.validateOrder()) {
            return;
        }

        this.setState({
            alert: [],
            canEditForm: false,
        });

        if (!this.state.orderId) {
            // create a new order
            api.post(window.Urls.api_create_order(), {
                email: this.state.email,
                newsletter: this.state.newsletter,
                addon: this.state.addon,
                price: this.state.total_price,
            }).then((response) => {
                console.log(response);
                this.setState({
                    alert: ['Your order is created.'],
                    sessionId: response.data.sid,
                    total_price: response.data.total_price,
                    canEditForm: false,
                    canPay: true,
                }, () => {
                    // additional work
                });
            }).catch((error) => {
                this.setState({
                    canEditForm: true,
                });
                this.apiErrorHandler(error);
            });
        } else {
            // any additional logic

        }
    }

    handlePaypalPayment(data, actions) {
        return actions.order.capture().then((details) => {
            api.post(window.Urls.api_paypal_payment(), {
                sid: this.state.sessionId,
                data: data,
                paypal_details: details,
            }).then(response => {
                // do something with response if necessary
                console.debug(response);
                document.location = window.Urls.order_status(this.state.sessionId);
            }).catch((error) => {
                console.log(error);
                var newAlerts = [...this.state.alert];
                newAlerts.push('Oops! Something went wrong when recording your payment. Please contact support. Error: ' + error.message);
                this.setState({
                    alert: newAlerts,
                });
            });
        });
    }

    handleEmailChange(e) {
        const res = /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/i;
        var valid = res.test(e.target.value);

        this.setState({
            email: e.target.value,
            emailValid: valid,
        });
    }

    updatePrice() {
        var price = 10;

        if (this.state.addon) {
            price = price + 10;
        }

        var tax = Math.round(price * this.props.tax_rate / 100, 2);
        this.setState({
            price: price,
            tax: tax,
            total_price: price + tax
        });
    }



    render() {
        return (
            <React.Fragment>
                <form>
                    <React.Fragment>
                        <div className="mt-lg-5 mb-lg-5 mb-3">
                            <label htmlFor="inputEmail" className="form-label"><i className="bi bi-envelope"></i> Email address</label>
                            <input id="inputEmail" type="email" className="form-control" aria-describedby="emailHelp" value={this.state.email} onChange={this.handleEmailChange} disabled={!this.state.canEditForm} />
                            <div id="emailHelp" className="form-text mb-2">
                                {!this.state.emailValid &&
                                    <span className='text-danger'>Please enter a valid email address. </span>
                                }
                                You'll receive a link to your order. Make sure it works.
                            </div>
                            <Form.Check
                                type="checkbox"
                                id="newsletter"
                                label="Receive product updates newsletter to this email"
                                checked={this.state.newsletter}
                                disabled={!this.state.canEditForm}
                                onChange={e => {
                                    this.setState({
                                        newsletter: !this.state.newsletter,
                                    });
                                }}
                            />
                        </div>
                    </React.Fragment>

                    <div className="mt-lg-5 mb-lg-5 mb-3">
                        <label htmlFor="addon" className="form-label"><i className="bi bi-wrench-adjustable"></i> Addon - 10$</label>

                        <div id="addonHelp" className="form-text mb-2">
                            Add addon to your order.
                        </div>
                        <Form.Check
                            type="checkbox"
                            id="addon"
                            label="Add on purchase"
                            checked={this.state.addon}
                            disabled={!this.state.canEditForm}
                            onChange={e => {
                                this.setState({
                                    addon: !this.state.addon,
                                }, () => { this.updatePrice(); });

                            }}
                        />
                    </div>
                    <div className="mb-lg-5 mb-3">
                        <label className="form-label"><i className="bi bi-credit-card"></i> Payment</label>

                        <div className="form-text">
                            <p>Current price is: {this.props.tax_rate == 0 ? this.state.price + '$' : this.state.price + '$ + VAT ' + this.props.tax_rate + '%'}
                            </p>
                            <p>Clicking the button below you agree to the Terms of Service</p>
                        </div>
                        {this.state.alert.length > 0 &&
                            <Alert variant="primary">
                                {this.state.alert.map((x, i) => {
                                    return (
                                        <div key={'alert' + i}>{x}</div>
                                    );
                                })}
                            </Alert>

                        }
                        {this.props.allow_new_orders && !this.state.canPay && (
                            this.state.canEditForm
                                ? <a href="#" onClick={this.handleCreateOrder} className="btn btn-primary">Place order and Proceed to Payment</a>

                                : <button className="btn btn-primary" disabled={true}><span className="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Creating...</button>)
                        }
                        {!this.props.allow_new_orders &&
                            <p>Sorry, we are not accepting new orders at the moment, check back later.</p>
                        }
                        {this.state.canPay &&
                            <div className="my-lg-5 my-3">
                                <PayPalScriptProvider
                                    options={{
                                        'client-id': this.props.paypal_client_id,
                                        currency: 'USD',
                                        debug: true,

                                    }}>
                                    <PayPalButtons
                                        style={{
                                            color: 'blue',
                                            shape: 'pill',
                                            label: 'checkout',
                                            tagline: false,
                                        }}
                                        createOrder={(data, actions) => {
                                            return actions.order.create({
                                                purchase_units: [{
                                                    description: 'Order ID: ' + this.state.sessionId,
                                                    amount: {
                                                        value: this.state.total_price,
                                                    },
                                                }],
                                            });
                                        }}
                                        onApprove={this.handlePaypalPayment} />
                                </PayPalScriptProvider>
                            </div>
                        }
                        {this.state.sessionId &&
                            <div className="mb-lg-5 mb-3">
                                <label className="form-label"><i className="bi bi-credit-card"></i> Your order</label>

                                <div className="form-text">
                                    Your order ID: {this.state.sessionId} <a target="_blank" href={window.Urls.order_status(this.state.orderId)}>View status</a>
                                </div>
                            </div>
                        }
                    </div>
                </form>
            </React.Fragment>
        );
    }
}

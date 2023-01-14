var Utils = {};

Utils.listClassMethodNames = function(instance, followPrototype)
{
    let props = [];
    let obj = Object.getPrototypeOf(instance);
    const endPrototype = (followPrototype ? Object.prototype : Object.getPrototypeOf(obj));

    while (obj !== endPrototype)
    {
        props = props.concat(Object.getOwnPropertyNames(obj));
        obj = Object.getPrototypeOf(obj);
    }

    return props.sort().filter((e, i, arr) => e != arr[i+1] && typeof(instance[e]) == 'function');
};

Utils.autoBindClass = function(instance, options)
{
    options = options || {};
    const followPrototype = options.followPrototype || false;
    const prefixes = options.prefixes || null;

    const methods = Utils.listClassMethodNames(instance, followPrototype);
    const filteredMethods = methods.filter((methodName) =>
        (methodName !== 'constructor' &&
         (!prefixes || prefixes.some((prefix) => methodName.indexOf(prefix) === 0)))
    );

    filteredMethods.forEach((methodName) => {
        instance[methodName] = instance[methodName].bind(instance);
    });

    return filteredMethods;
};

export {
    Utils,
};

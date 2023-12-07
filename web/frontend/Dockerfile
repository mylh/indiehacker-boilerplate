FROM node:18

WORKDIR /app/

ADD package.json /app/package.json
RUN npm install
ADD . /app/

RUN npm i -g vite

RUN chown -R node /app/node_modules

CMD ["npm", "run", "dev"]

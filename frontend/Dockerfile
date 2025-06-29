# Use Node to build
FROM node:18-alpine AS build

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm install

COPY . .

RUN npm run build

# Use nginx to serve
FROM nginx:alpine

# Copy built react files
COPY --from=build /app/build /usr/share/nginx/html

# Copy your nginx config
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]

# --- Base build stage ---
FROM node:alpine3.22 as base
WORKDIR /app
COPY package*.json ./
RUN npm install


# --- Dev stage (live code mount) ---
FROM base AS dev
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "8080"]

# --- Prod stage ---
FROM base AS build
COPY . .
RUN npm run build -- --mode production

FROM nginx:alpine AS prod
COPY --from=build /app/dist /usr/share/nginx/html
COPY default.conf /etc/nginx/conf.d/default.conf

EXPOSE 8080
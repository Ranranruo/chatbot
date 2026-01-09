FROM node:22

ARG API_BASE_URL
ENV VITE_API_BASE_URL=$API_BASE_URL

WORKDIR /app
COPY package*.json ./
RUN npm ci --omit=dev
COPY . .
RUN npm run build

CMD ["npm", "run", "dev"]
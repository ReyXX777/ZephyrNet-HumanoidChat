# Stage 1: Build the React application
FROM node:16 as build

# Set the working directory for the build stage
WORKDIR /app

# Copy package.json and package-lock.json to install dependencies
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code into the container
COPY . .

# Build the React application for production
RUN npm run build

# Stage 2: Serve with Nginx
FROM nginx:latest

# Copy built files from Stage 1 to Nginx's HTML directory
COPY --from=build /app/build /usr/share/nginx/html

# Copy custom Nginx configuration file (optional, if you have specific routing needs)
# Uncomment the following line if you have a custom Nginx configuration file
# COPY nginx/frontend.conf /etc/nginx/conf.d/default.conf

# Expose port 80 for the container to be accessible
EXPOSE 80

# Start Nginx server (running in the foreground)
CMD ["nginx", "-g", "daemon off;"]

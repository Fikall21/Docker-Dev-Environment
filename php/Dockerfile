FROM php:8.2-fpm

# Install dependensi sistem termasuk libpq-dev untuk PostgreSQL
RUN apt-get update && apt-get install -y \
    libpng-dev \
    libjpeg-dev \
    libfreetype6-dev \
    libpq-dev \
    zip \
    unzip \
    git \
    && docker-php-ext-install pdo pdo_mysql pdo_pgsql gd

WORKDIR /var/www/html
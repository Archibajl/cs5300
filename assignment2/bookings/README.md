# Movie Booking System

A Django-based movie theater booking system with REST API endpoints and web templates for managing movie showings, seat reservations, and booking history.

## Features

- **Movie Management**: View available movies with titles, descriptions, release dates, and durations
- **Seat Booking**: Check seat availability and booking status
- **Booking History**: Track all movie bookings with dates
- **REST API**: JSON API endpoints for programmatic access
- **Web Interface**: HTML templates for user-friendly interaction

## Project Structure

```
bookings/
├── bookings/
│   ├── models.py           # Database models (Movies, Seats, Bookings)
│   ├── serializers.py      # REST framework serializers
│   ├── views.py            # View functions and API views
│   ├── urls.py             # URL routing configuration
│   ├── settings.py         # Django settings
│   ├── templates/          # HTML templates
│   │   ├── base.html
│   │   ├── movie_list.html
│   │   ├── seat_booking.html
│   │   └── booking_history.html
│   └── test/               # Unit tests
│       ├── testModels.py
│       └── testSerializers.py
├── manage.py
└── db.sqlite3
```

## Models

### Movies
- `title`: Movie title (max 200 characters)
- `description`: Movie description (max 500 characters)
- `releaseDate`: Release date
- `duration`: Movie duration

### Seats
- `seatNumber`: Seat identifier (max 10 characters)
- `bookingStatus`: Availability status (boolean)
- `published`: Date published

### Bookings
- `movie`: Foreign key to Movies
- `seat`: Foreign key to Seats
- `bookingDate`: Date of booking

## API Endpoints

### REST API
- `GET /api/movies/` - List all movies
- `GET /api/seats/` - List all seats and availability
- `GET /api/bookings/` - List all bookings
- `POST /api/bookings/create/` - Create a new booking

### Web Pages
- `GET /` - Base/home page
- `GET /movies/` - Browse available movies
- `GET /seats/` - View seat map and availability
- `GET /history/` - View booking history
- `GET /admin/` - Django admin interface

## Setup

### Prerequisites
- Python 3.x
- Django 4.2.11
- Django REST Framework

### Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install django djangorestframework
   ```

3. Apply migrations:
   ```bash
   python manage.py migrate
   ```

4. Create a superuser (optional):
   ```bash
   python manage.py createsuperuser
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the application at `http://127.0.0.1:8000/`

## Testing

Run unit tests with pytest:
```bash
pytest
```

Test files are located in `bookings/test/`:
- `testModels.py` - Model tests
- `testSerializers.py` - Serializer tests

## Database

The project uses SQLite (`db.sqlite3`) for development. For production, configure a different database in `bookings/settings.py`.

## Configuration

Key settings in `bookings/settings.py`:
- `DEBUG = True` - Development mode (set to False for production)
- `ALLOWED_HOSTS = []` - Configure allowed hosts for production
- `SECRET_KEY` - Change for production deployment
- `REST_FRAMEWORK` - Configured to use JSON renderer

## Development Notes

- The project uses Django REST Framework for API functionality
- Templates are stored in `bookings/templates/`
- Static files served via Django's static file handling
- All API responses return JSON format

## Security Warnings

⚠️ **Before deploying to production:**
1. Set `DEBUG = False`
2. Change `SECRET_KEY` to a secure random value
3. Configure `ALLOWED_HOSTS`
4. Use a production-grade database
5. Set up proper static file serving
6. Enable HTTPS

## License

This project is for educational purposes (CS5300 Assignment 2).

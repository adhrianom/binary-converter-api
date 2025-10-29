# Binary Conversor API

REST API and Frontend for converting decimal numbers to IEEE 754 (32-bit) binary representation.

---

## Deploy

- **Frontend (React):** [Vercel](https://vercel.com/)
- **Backend (Django):** [Render](https://render.com/)

---

## Demo

- **Frontend:** [https://binary-conversor.vercel.app/](https://binary-conversor.vercel.app/)
- **Backend:** [https://binary-conversor-api.onrender.com/](https://binary-conversor-api.onrender.com/)

---

## Project Structure

```
binary_conversor_API/
├── backend/         # Backend code (Django)
│   ├── manage.py
│   ├── binary_conversor/
│   └── core/
├── frontend/        # Frontend code (React + Vite)
│   ├── src/
│   ├── public/
│   └── ...
├── venv/            # Python virtual environment (do not version)
├── README.md
└── ...
```

---

## Backend (Django)

### Description

The backend receives HTTP requests and converts decimal numbers to IEEE 754 binary representation.

### Main points

- **Framework:** Django
- **Main endpoint:**  
  `POST /core/converter/`  
  Receives a JSON with the field `number` and returns the IEEE 754 representation.

### Usage example

**Request:**
```json
{
  "number": 5.75
}
```

**Response:**
```json
{
  "number_received": 5.75,
  "ieee754": {
    "signal": 0,
    "exponent": "10000001",
    "mantissa": "01110000000000000000000"
  }
}
```

### How to run locally

1. **Clone the repository:**
   ```bash
   git clone <REPOSITORY-URL>
   cd binary_conversor_API
   ```

2. **Create and activate the virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r backend/requirements.txt
   ```

4. **Run migrations:**
   ```bash
   cd backend
   python manage.py migrate
   ```

5. **Start the server:**
   ```bash
   python manage.py runserver
   ```

### Deploy on Render

- Create a new web service on [Render](https://render.com/) pointing to the `backend` directory.
- Set the build command:  
  `pip install -r requirements.txt && python manage.py migrate`
- Set the start command:  
  `gunicorn binary_conversor.wsgi`
- Add the required environment variables (e.g., `DJANGO_SECRET_KEY`, `ALLOWED_HOSTS`).

---

## Frontend (React + Vite)

### Description

Web interface for users to input numbers, view the conversion, and interact with the calculator.

### How to run locally

1. **Go to the frontend folder:**
   ```bash
   cd frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start the development server:**
   ```bash
   npm run dev
   ```

### Deploy on Vercel

- Log in to [Vercel](https://vercel.com/) and import the repository.
- Choose the `frontend` directory as the project root.
- Vercel will automatically detect Vite/React projects.
- Set the environment variable `VITE_API_URL` (if needed) to point to the Render backend.

---

## Notes

- The frontend communicates with the backend via REST API.
- The backend may take a few seconds to "wake up" on Render (free tier).
- The Python virtual environment (`venv`) **should not be versioned**.

---

## Reference

- Conversion logic: [binary_conversor_IEEE](https://github.com/adhrianom/binary_conversor_IEEE)

## License

This project follows the license of the original repository.
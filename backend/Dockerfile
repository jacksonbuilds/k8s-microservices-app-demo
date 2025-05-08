FROM python:3.11-slim

# Create a non-root user and group
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

WORKDIR /app

# Copy requirements and install
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Set permissions for the app directory
RUN chown -R appuser:appgroup /app

# Switch to the non-root user
USER appuser

# Run with gunicorn (app:app refers to app.py -> app variable)
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]

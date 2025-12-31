# 1. Lightweight base image
FROM python:3.12-slim

# 2. Create non-root user
RUN useradd -m appuser

# 3. Set working directory
WORKDIR /app

# 4. Copy dependency file
COPY requirements.txt .

# 5. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy application code
COPY app.py .

# 7. Change ownership
RUN chown -R appuser:appuser /app

# 8. Switch to non-root user
USER appuser

# 9. Expose application port (documentation only)
EXPOSE 5000

# 10. Run application
CMD ["python", "app.py"]

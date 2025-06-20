# Python Learning Platform - Deployment Guide

This guide provides multiple deployment options for your Python Learning Platform.

## Project Structure

```
python-learning-platform/
├── app.py                      # Main application
├── pages/                      # Streamlit pages
│   ├── 00_register.py         # User registration/login
│   ├── 01_tutorials.py        # Learning tutorials
│   ├── 02_exercises.py        # Coding exercises
│   ├── 03_progress.py         # Progress tracking
│   ├── 04_playground.py       # Code playground
│   ├── 05_community.py        # Community features
│   └── 06_forum.py            # Discussion forum
├── utils/                      # Utility modules
│   ├── auth_manager.py        # Authentication
│   ├── code_executor.py       # Safe code execution
│   ├── db_adapter.py          # Database operations
│   ├── forum_manager.py       # Forum management
│   └── progress_tracker.py    # Progress tracking
├── data/                       # Content data
│   ├── exercises.py           # Exercise definitions
│   └── tutorials.py           # Tutorial content
├── database/                   # Database models
│   ├── connection.py          # DB connection
│   └── models.py              # SQLAlchemy models
├── .streamlit/                 # Streamlit config
│   └── config.toml            # Server configuration
├── deploy_requirements.txt     # Python dependencies
├── Dockerfile                  # Docker configuration
├── docker-compose.yml          # Multi-container setup
├── init.sql                    # Database initialization
└── runtime.txt                 # Python version
```

## Deployment Options

### 1. Streamlit Community Cloud (Recommended for beginners)

**Steps:**
1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub account
4. Select your repository
5. Set main file path: `app.py`
6. Add environment variables in Advanced settings:
   - `PGHOST`: Your PostgreSQL host
   - `PGPORT`: 5432
   - `PGDATABASE`: Your database name
   - `PGUSER`: Your database username
   - `PGPASSWORD`: Your database password

**Pros:** Free, easy setup, automatic deployments
**Cons:** Requires external PostgreSQL database

### 2. Heroku Deployment

**Prerequisites:**
- Heroku account
- Heroku CLI installed

**Steps:**
1. Create `Procfile`:
   ```
   web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
   ```

2. Rename `deploy_requirements.txt` to `requirements.txt`

3. Deploy:
   ```bash
   heroku create your-app-name
   heroku addons:create heroku-postgresql:mini
   git push heroku main
   ```

**Pros:** Built-in PostgreSQL, custom domains, scaling
**Cons:** Paid after free tier limits

### 3. Docker Deployment

**Local Testing:**
```bash
# Start with Docker Compose
docker-compose up

# Access at http://localhost:8501
```

**Production Deployment:**
```bash
# Build image
docker build -t python-learning-platform .

# Run with external database
docker run -p 8501:8501 \
  -e PGHOST=your-db-host \
  -e PGPORT=5432 \
  -e PGDATABASE=your-db-name \
  -e PGUSER=your-username \
  -e PGPASSWORD=your-password \
  python-learning-platform
```

### 4. Railway Deployment

**Steps:**
1. Connect Railway to your GitHub repo
2. Add PostgreSQL plugin
3. Set environment variables automatically
4. Deploy with one click

**Pros:** Simple setup, automatic scaling, built-in database
**Cons:** Paid service

### 5. DigitalOcean App Platform

**Steps:**
1. Create new app from GitHub
2. Configure build settings:
   - Build Command: `pip install -r deploy_requirements.txt`
   - Run Command: `streamlit run app.py --server.port=8080 --server.address=0.0.0.0`
3. Add managed PostgreSQL database
4. Configure environment variables

## Database Setup

### Option 1: Managed Database Services
- **ElephantSQL** (free PostgreSQL)
- **Supabase** (free PostgreSQL with dashboard)
- **AWS RDS** (paid, production-ready)
- **Google Cloud SQL** (paid, production-ready)

### Option 2: Self-hosted Database
Use the included `docker-compose.yml` for local development or VPS deployment.

## Environment Variables

Set these variables in your deployment platform:

```bash
PGHOST=your-database-host
PGPORT=5432
PGDATABASE=python_learning_platform
PGUSER=your-username
PGPASSWORD=your-secure-password
```

## Post-Deployment Steps

1. **Database Initialization:** The `init.sql` file will automatically create all necessary tables and sample data.

2. **Create Admin User:** Register the first user through the web interface.

3. **Test Features:**
   - User registration and login
   - Tutorial completion
   - Exercise submission
   - Forum posting
   - Progress tracking

## Troubleshooting

### Common Issues:

1. **Database Connection Errors:**
   - Verify environment variables are set correctly
   - Check database server is running and accessible
   - Ensure firewall allows connections

2. **Port Issues:**
   - Streamlit Community Cloud uses port 8501
   - Heroku assigns port via $PORT variable
   - Local development uses port 5000

3. **Dependencies:**
   - Ensure `deploy_requirements.txt` includes all packages
   - Some platforms may require specific versions

### Performance Optimization:

1. **Database Indexing:** The `init.sql` includes optimized indexes
2. **Caching:** Streamlit automatically caches data
3. **Session State:** Minimized database queries through smart caching

## Security Considerations

1. **Password Security:** Uses bcrypt hashing
2. **Code Execution:** Restricted execution environment
3. **SQL Injection:** Parameterized queries throughout
4. **Environment Variables:** Sensitive data stored securely

## Monitoring and Maintenance

1. **Logs:** Check platform-specific logs for errors
2. **Database Backup:** Set up regular backups
3. **Updates:** Monitor dependencies for security updates
4. **Performance:** Monitor response times and database queries

## Cost Estimates

### Free Options:
- Streamlit Community Cloud: Free (with external database)
- Heroku Free Tier: Free for 1000 hours/month

### Paid Options:
- Heroku Hobby: $7/month + database costs
- Railway: Starting at $5/month
- DigitalOcean: Starting at $5/month

## Support

For deployment issues:
1. Check platform-specific documentation
2. Review error logs carefully
3. Verify all environment variables
4. Test database connectivity

The platform is designed to work on any Python hosting service that supports Streamlit and PostgreSQL.
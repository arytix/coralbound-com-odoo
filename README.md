# Coralbound Odoo Instance

This repository contains the Docker configuration and custom modules for Coralbound's Odoo instance deployed on Railway.

## Repository Structure

```
.
├── Dockerfile              # Main Docker configuration
├── entrypoint.sh          # Container startup script
├── custom-addons/         # Custom Odoo modules
│   ├── coralbound_theme/  # Custom theme module
│   └── navbar_red/        # Example module (can be removed)
```

## Custom Modules

### Coralbound Theme (`coralbound_theme`)

Customizes the Odoo interface with Coralbound branding:

- Custom logo
- Primary and secondary colors
- Comprehensive UI styling

To customize the theme:

1. Place your logo in `custom-addons/coralbound_theme/static/src/img/logo.jpg`
2. Adjust colors in `custom-addons/coralbound_theme/static/src/css/theme.css`:
   ```css
   :root {
     --primary-color: #2b6cb0; /* Your primary color */
     --secondary-color: #4299e1; /* Your secondary color */
     --primary-hover: #2c5282; /* Darker shade for hover */
     --secondary-hover: #3182ce; /* Darker shade for hover */
   }
   ```

## Development

### Prerequisites

- Docker
- Railway CLI (optional)

### Local Development

1. Build the Docker image:

   ```bash
   docker build -t coralbound-odoo .
   ```

2. Run the container:
   ```bash
   docker run -p 8069:8069 coralbound-odoo
   ```

### Adding Custom Modules

1. Create a new directory in `custom-addons/`
2. Follow the standard Odoo module structure
3. Rebuild the Docker image

## Deployment

This instance is deployed on Railway. The deployment process is automated through Railway's GitHub integration.

### Environment Variables

Required environment variables in Railway:

- `ODOO_DATABASE_HOST`
- `ODOO_DATABASE_PORT`
- `ODOO_DATABASE_USER`
- `ODOO_DATABASE_PASSWORD`
- `ODOO_DATABASE_NAME`
- `ODOO_SMTP_HOST`
- `ODOO_SMTP_PORT_NUMBER`
- `ODOO_SMTP_USER`
- `ODOO_SMTP_PASSWORD`
- `ODOO_EMAIL_FROM`

### Volumes

- A 50GB volume is mounted at `/var/lib/odoo` for data persistence

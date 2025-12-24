# simulator-backend

🚗 AutoWrap 3D Backend
AutoWrap 3D is a robust Django-based API designed to power a real-time car wrap simulation environment. It manages high-fidelity 3D assets, vinyl material properties, and user configurations, providing a seamless bridge between 3D designers and web-based rendering engines like Three.js.

🛠 Tech Stack
Framework: Django 6.0 (Python)

Database: PostgreSQL (Production), SQLite (Development)

Asset Management: Cloudinary (3D .glb hosting and optimization)

API: Django Rest Framework (DRF)

3D Format: GLB (glTF Binary)

🚀 Key Features
Dynamic 3D Asset Pipeline: Automatic mesh optimization and delivery of .glb models.

Material Registry: A database of wrap finishes including Matte, Gloss, Satin, and Chrome with specific hexadecimal color mapping.

Admin Dashboard: Built-in UI for non-technical staff to add new vehicles and materials without writing code.

Scalable API: Clean endpoints for fetching vehicle metadata and model URLs.

📁 Project Structure
Plaintext

autowrap_backend/
├── config/              # Project settings and URLs
├── vehicles/            # App for car models and metadata
├── materials/           # App for vinyl wrap finishes and colors
├── users/               # Custom user profiles and saved builds
├── manage.py            # Django command-line utility
└── requirements.txt     # Python dependencies
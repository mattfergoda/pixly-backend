# Pixly Backend

A Flask backend for a photo storing and editing application. It utilizes the [Pillow](https://pillow.readthedocs.io/en/stable/) library for photo manipulation, AWS S3 for blob storage and photo versioning, and a PostgreSQL database primarily for storing photo metadata, by which the user can search in the frontend.

[Frontend Repo](https://github.com/mattfergoda/pixly-frontend)

[Live App Demo](https://pixly.demo.mattfergoda.me/)  

> **Note:**  It can take a few minutes for the backend demo to spin up. The app may appear unresponsive during that time.

## Future Work
- Add unit and integration tests.
- Refactor editing logic to more easily allow for multiple possible edits. For example, a request could contain `"edit": "bw"`, `"edit": "rotate"`, etc. instead of the current `"bw" : True`. 
- Add other edits beyond black and white.
- Protect routes with user authentication and authorization.
- Allow a user to rollback an edit by using S3's built-in versioning.
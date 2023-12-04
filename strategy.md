

DATA REQUIRMENTS

- storing images on s3

- obtain exif data (when image is uploaded?) and store in database for user search feature

- pillow, basically


STACK
postgres
sqlalchemy
python
flask
react
css, reactstrap?


SEARCH
- simple search by file name using ILIKE ala jobly backend 1 hour
- postgres full text search too much?


FRONTEND
REMEMBER CORS ISSUES, test our flask-cors setup

`NavBar` component
`RouteList` component
`Homepage` component with links to

- List of All images (`ImageList`)
    - `Search` bar component
    - each `ImageDetail` component has/is a link to edit that image

- `UploadForm` for uploading image

- `EditForm` component
    - radio buttons?
    - black and white
    - sepia?

## Nice to haves once done
- Alerts in front end
- description text area?
- JPEG format validation
- Styling
- Tests
- More image edits
- last modified
- add caption/description to search
- adding new image doesn't show up right away in all images
- undo edit


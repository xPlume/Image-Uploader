# Image_Uploader

> A simple Django web application handling image uploading with a modern intuitive UI.

---

## Table of Contents

- [Project Description](#project-description)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Implementation Details](#implementation-details)

---

## Project Description

With the massive popularity of social media and other similar applications, users are very familiar with image uploading on different platforms. Developing a web application, handling both the backend and frontend to recreate a very intuitive and modern designed UI for image uploading is, however, quite tricky.

The goal of this project is to go way beyond the default file input provided by HTML and CSS, in order to obtain a truly extensive, complete, yet intuitive image upload feature. In one single field, users will be able to upload, preview, re-organize, and delete any images they wish to upload. The backend then manages which images have been uploaded, in which order, and which ones have been deleted.

---


## Tech Stack

- Framework: [Django](https://www.djangoproject.com/)
- CSS: [Bootstrap](https://getbootstrap.com/)


## Getting Started


### Prerequisites

Make sure you have the following installed on your system:

- **Python** (>= 3.10 recommended)
- **pip** (Python package manager)
- **virtualenv** (Optional but recommended)
- **Git**

You can verify your Python and pip installation with:

```bash
python --version
pip --version
```

### Installation

1. Clone the repository:

```bash
git clone https://github.com/xPlume/Image-Uploader.git
```

2. Navigate to the project root:
```bash
cd Image-Uploader
```

3. (Optional) Create and activate a virtual environment.
```bash
python -m venv [VENV_NAME]
source [VENV_NAME]/bin/activate
```

4. Install the Python dependencies:
```bash
pip install -r requirements.txt
```

5. Navigate to the Project directory
```bash
cd Project
```

6. Apply database migrations:
```bash
python manage.py migrate
```

7. Create a superuser to access the Django admin:
```bash
python manage.py createsuperuser
```

8. Start the development server:
```bash
python manage.py runserver
```

---

## Implementation Details

The initial goal of this project was to make it as pluggable as possible. That has revealed to be quite difficult. The backend (views.py) is heavily tied to the structure of the database (models.py). The frontend (templates) is also heavily linked to the backend, making a general solution pluggable in other projects without any consideration for the architecture unfeasible. However, it does not mean that the implementation brought in this project is irrelevant. Lots of copy-pasting can still be done to obtain the same results in other Django project, without too much of a headache. 

For this project, we have two tables in our database. Gallery and Images. A gallery can have various images. One image is tied to one gallery. When users upload images, they are uploading them to a specific gallery (which could be thought of as an individual publication in a social media for example). Both of these tables can be found in the **Project/gallery/model/** directory.

The core of the project is in the backend, handling the complex image uploading. The file handling the heavy lifting is located at the following path: **Project/gallery/views/gallery_edit.py**. It allows users to upload, delete, and re-order images in any way they wish. Note here that this file handles the very first publication of images (create), the modification of these images (update), as well as allowing the users to remove any and all images (delete). This file uses direct references to the names of both the tables Gallery and Images, and also their different attributes. Any modifications of these parameters in the database will require this file to be updated alongside those.

Finally, to display the content, we use two different HTML files located at the following path: **Project/gallery/templates/gallery/**. The first one, **gallery_edit.html** is being used to display the content of the page "around" the input field. Do note that we do need to load the Sortables javascript library in the head of that file. Note as well that we specify a very specific CSS style: *.galleryimg*. This one here is used to specify the aspect ratio of the images that will be displayed in the upload field. 

Finally we have the file **image_upload_field.html**. As the name suggests, this one handles the display of the upload field. It was kept separate as it can be a bit complex and should, in the best case scenario, not need any modifications at all! It is really meant to be copy-pasted in your Django project. Just don't forget to properly reference it where you want the image upload field.

---
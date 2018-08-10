# Face equal-ais service

The face equalization service base URL is at

`https://equal-ais.appspot.com`

## How do I start this?

### On Google Cloud App Engine
1. Install/configurature [google cloud SDK](https://cloud.google.com/sdk/)
1. In a terminal, run `gcloud app deploy equalais_rest_server/equal_ais_rest_api_app.yaml --project equal-ais --verbosity=info`

### Locally

1. Install/configurature [pipenv](https://docs.pipenv.org/)
1. In the top-level folder, run `pipenv install`
1. run `face_equal_ias_service.py`

## Notes

* To create the requirements file from a pipfile, run `pipenv lock --requirements > ./equalais_rest_server/requirements.txt`
    * For now you've got to pull dlib out of requirements! (Having issues getting it to run on Google App Engine machines.)

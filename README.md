# ProjectClaims

#### How to ejecute the application?

1. Open terminal.
2. Situate in project path.
3. Build docker with the command:
`$: docker-compose build`
4. Up docker with the command:
`$: docker-compose up`

#### How to ejecute tests?
1. Open terminal.
2. Entry in docker.
`$: docker exec -ti projectclaims_django_1 /bin/bash`
3.  Ejecute command:
`$: python manage.py test`

#### APIS:
- Calculate how many square inches of office wall are within two or more claims.

http://localhost:8000/count_occupied_inch/
- Which is the ID of the only claim that doesn't overlap

http://localhost:8000/list_full_claim_ids/

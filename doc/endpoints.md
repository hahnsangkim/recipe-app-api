## public

/api/recipe/ purpose: show the links to tags and ingredients; input: GET-{}
![](/img/01.png)

/api/user/create/ purpose: create a user; input: POST-{email, password, name}; output: {email, name}
![](/img02.png)

## private
### Authentication
/api/user/token/  purpose: get a token; input: POST-{email, password}; output: {token}
![](/img03.png)

/api/user/me/     purpose: access priviledge; input: {Authorization, token}; output: access
![](/img04.png)

### admin
/admin/

### list view
/api/recipe/tags/ purpose: show the tag list and add one to it; input: GET or POST-{name, token}; output: [{id, name}]
![](/img05.png)

/api/recipe/ingredients/ purpose: show the ingredient list and add one to it; input: GET or POST-{name, token}; output: [{id, name}]
![](/img06.png)

/api/recipe/recipes/ purpose: list recipes; input: GET or POST-{title, ingredients, tags, time, price, link}; output: [{}, {}]
![](/img07.png)
![](/img08.png)

### detail view
/api/recipe/recipes/1/ purpose: show recipe detail; GET or PUT-{title, ingredients, tags, time, price, link}; output: {}
![](/img09.png)
![](/img10.png)

/api/recipe/recipes/1/upload-image purpose: upload an image; Form PUT-{file path}; output: {id, image:url}
![](/img11.png)
click image:url http://127.0.0.1:8000/media/uploads/recipe/c283f222-d32b-4bef-8db1-4e5b1c7ecebf.png


### filtering
/api/recipe/recipes/?ingredients=1 purpose: filter with ingredient; GET; output: [{id, title, ingredients[], tags[], time, price, link}]
![](/img12.png)
![](/img13.png)

/api/recipe/recipes/?tags=1 purpose: filter with tags; GET; output: [{id, title, ingredients[], tags[], time, price, link}]
/api/recipe/recipes/?tags=1&ingredients=1 purpose: filter ; GET; output: [{id, title, ingredients[], tags[], time, price, link}]
![](/img14.png)
![](/img15.png)

/api/recipe/tags/?assigned_only=1 purpose: make sure to get tags with assigned to recipes; output: tags assigned only
/api/recipe/tags/?assigned_only=0 purpose: list all tags; output: tags
![](/img16.png)

/api/recipe/ingredients/?assigned_only=1 purpose: make sure to get ingredients with assigned to recipes
![](/img17.png)
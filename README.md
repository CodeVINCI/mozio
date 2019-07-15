# mozio api

## *Create Providers, create their areas of service as polygons, update polygons, delete polygons, query the polygons that serve the customer at paerticular longitude and lattitude*

## Create Provider

``` 
*http://18.188.6.18/createprovider/ 
```
*create a json in the content and post the data to create a new provider.

*Example json:
``` 
{
"name":"laxmi travels",
"email": "laxmi@laxmitravels.com",
"phone_number": "+919149787049",
"currency": "INR",
"language": "english"
 }

```

*this will return you a token of the provider which is unique identity of the provider.

## Create Polygon of a Provider
``` 
*http://18.188.6.18/createpolygon/ 
```
*create a json in the content and post the data to create a new polygon.

*Example json
```
{
"name": "laxmitravelsdelhi",
"token": "1dDtEJpErwQNLJ2GBs0gUrhbFwEOn8SR",
"coordinates": [[ [100.0, 0.0], [101.0, 0.0], [101.0, 1.0], [100.0, 1.0], [100.0, 0.0] ]]
}
```


## Get all the polygons of a Provider

``` 
*http://18.188.6.18/api/mypolygons/?token=OUGMfgMngPtBDVprr3ZK3L5MfcNnmo7n 
```
*token of the provider as a query in the url will get you all the polygons served by the provider


## Update Polygon

``` 
*http://18.188.6.18/updatepolygon/ 
```
*create a json in the content and post the data to update a polygon.

*Example json
```
{
"name": "laxmitravelsdelhi",
"token": "1dDtEJpErwQNLJ2GBs0gUrhbFwEOn8SR",
"coordinates": [[ [105.0, 0.0], [108.0, 0.0], [108.0, 1.0], [105.0, 1.0], [105.0, 0.0] ]]
}
```

## Delete Polygon

``` 
*http://18.188.6.18/updatepolygon/ 
```
*create a json in the content and post the data to update a polygon.
*Example json
```
{
"name": "laxmitravelsdelhi",
"token": "1dDtEJpErwQNLJ2GBs0gUrhbFwEOn8SR"
}
```

## Query for polygons containing a point(geolocation lattitude and longitude)

``` 
*http://18.188.6.18/api/polygons/?lng=105&lat=55 
```

*this is how you query all the providers who have services at your current location

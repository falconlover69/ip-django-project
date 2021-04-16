from import_export import resources
from .models import Posts

class PostsResource(resources.ModelResource) : 
    class Meta:
        model = Posts
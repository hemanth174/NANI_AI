from django.db import models

class Command(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class UserQuery(models.Model):
    query_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.query_text[:50]  # Return the first 50 characters of the query text

class Response(models.Model):
    user_query = models.ForeignKey(UserQuery, on_delete=models.CASCADE)
    response_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.response_text[:50]  # Return the first 50 characters of the response text
from django.db import models

class Order(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    parcel = models.ForeignKey('parcel_app.Parcel', on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

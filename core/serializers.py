from rest_framework import serializers

class HandlerSerializer(serializers.Serializer):
    user_email = serializers.EmailField()
    duration = serializers.IntegerField()
    plan_type = serializers.CharField()
    discount_enabled = serializers.BooleanField()

    def validate_discount_enabled(self,value):
        value = True if value == "True" else False
        return value



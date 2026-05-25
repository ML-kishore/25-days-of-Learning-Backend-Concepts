from .serializers import HandlerSerializer
from .models import GymMemberDetails
from rest_framework.response import Response

class GymServiceLayer:

    @staticmethod
    def process_membership_fee(data):

        #apply business rule
        base_rate = 2000 if data['plan_type'] == 'premium' else 1000
        final_amount = base_rate * data['duration']


        #rule 2 : apply discount 
        #checking the discount_enabled datatype is boolean -->
        print(type(data['discount_enabled']))
        if data['discount_enabled'] is True:
            final_amount = 0.90 * final_amount
            
        # calculate_record

        subscription_record = GymMemberDetails.objects.create(
            user_email = data['user_email'],
            plan = data['plan_type'],
            duration = data['duration'],
            final_billing = final_amount
        )

        return {"status" : "success" , "billing" : final_amount , "id" : subscription_record.id}
    

        
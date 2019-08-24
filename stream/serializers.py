from rest_framework import serializers

class PurrSerializer(serializers.ModelSerializer):

    def init(self):
        print("wut?")

from rest_framework import serializers

class FinalMarkSerializer(serializers.Serializer):
    student_id = serializers.IntegerField()
    mark = serializers.DecimalField(max_digits=5, decimal_places=2)
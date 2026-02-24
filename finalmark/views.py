# final/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import FinalMark
from .serializers import FinalMarkSerializer

class CreateFinalMarkView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = FinalMarkSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        student_id = serializer.validated_data["student_id"]
        mark_value = serializer.validated_data["mark"]

        obj, created = FinalMark.objects.update_or_create(
            student_id=student_id,
            teacher=request.user,
            defaults={"mark": mark_value}
        )

        return Response({
            "student_id": student_id,
            "teacher_id": request.user.id,
            "mark": str(obj.mark),
            "created": created
        })
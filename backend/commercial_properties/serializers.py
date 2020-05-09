from rest_framework import serializers

from .models import CommercialPremises, VideoCommercialPremises, ImagesCommercialPremises, FloorPlansCommercialPremises


class ImagesCommercialPremisesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagesCommercialPremises
        fields = '__all__'


class FloorPlansCommercialPremisesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FloorPlansCommercialPremises
        fields = '__all__'


class VideoCommercialPremisesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoCommercialPremises
        fields = '__all__'


class CommercialPremisesListSerializer(serializers.ModelSerializer):
    region = serializers.SlugRelatedField(slug_field='name', read_only=True)
    city = serializers.SlugRelatedField(slug_field='name', read_only=True)
    district = serializers.SlugRelatedField(slug_field='name', read_only=True)
    residential_complex = serializers.SlugRelatedField(slug_field='name', read_only=True)
    cooker_hood = serializers.SlugRelatedField(slug_field='name', read_only=True)

    # скорее всего в fixed_agent нужен будет только id
    fixed_agent = serializers.SlugRelatedField(slug_field='username', read_only=True, many=True)
    floor = serializers.SlugRelatedField(slug_field='num_floor', read_only=True, many=True)
    relative_location = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    purpose_commercial_premise = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    business_category = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    communication_systems = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    type_entrance = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)

    images_commercial_premises = ImagesCommercialPremisesListSerializer(many=True, read_only=True)
    floorplans_commercial_premises = FloorPlansCommercialPremisesListSerializer(many=True, read_only=True)
    video_commercial_premises = VideoCommercialPremisesListSerializer(many=True, read_only=True)

    class Meta:
        model = CommercialPremises
        fields = '__all__'


class CommercialPremisesDetailSerializer(serializers.ModelSerializer):
    region = serializers.SlugRelatedField(slug_field='name', read_only=True)
    city = serializers.SlugRelatedField(slug_field='name', read_only=True)
    district = serializers.SlugRelatedField(slug_field='name', read_only=True)
    residential_complex = serializers.SlugRelatedField(slug_field='name', read_only=True)
    cooker_hood = serializers.SlugRelatedField(slug_field='name', read_only=True)

    # скорее всего в fixed_agent нужен будет только id
    fixed_agent = serializers.SlugRelatedField(slug_field='username', read_only=True, many=True)
    floor = serializers.SlugRelatedField(slug_field='num_floor', read_only=True, many=True)
    relative_location = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    purpose_commercial_premise = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    business_category = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    communication_systems = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    type_entrance = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)

    images_commercial_premises = ImagesCommercialPremisesListSerializer(many=True, read_only=True)
    floorplans_commercial_premises = FloorPlansCommercialPremisesListSerializer(many=True, read_only=True)
    video_commercial_premises = VideoCommercialPremisesListSerializer(many=True, read_only=True)

    class Meta:
        model = CommercialPremises
        # exclude = ('is_active',)  # исключает поля
        fields = '__all__'


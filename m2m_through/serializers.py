from pprint import pprint

from rest_framework import serializers

from .models import Marathon, MarathonChallenge, Challenge


class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = '__all__'


class MarathonChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarathonChallenge
        fields = '__all__'


class MarathonReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marathon
        fields = '__all__'
        depth = 1

    def to_representation(self, instance):
        result = super().to_representation(instance)
        challenges = result.get('challenges')
        challenge_ids = [challenge['id'] for challenge in challenges]
        marathon_challenges = MarathonChallenge.objects \
            .filter(marathon=instance, challenge_id__in=challenge_ids)
        result['marathon_challenges'] = MarathonChallengeSerializer(marathon_challenges, many=True).data
        return result


class MarathonChallengeWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarathonChallenge
        exclude = ['marathon']


class MarathonWriteSerializer(serializers.ModelSerializer):
    marathon_challenge = MarathonChallengeWriteSerializer()

    class Meta:
        model = Marathon
        fields = '__all__'
        depth = 1

    def create(self, validated_data):
        pprint(validated_data)
        marathon_challenge = validated_data.pop('marathon_challenge')
        marathon_obj = Marathon.objects.create(**validated_data)
        marathon_challenge_obj = MarathonChallenge.objects.create(**marathon_challenge, marathon=marathon_obj)
        # marathon_obj.marathonchallenge_set.add(marathon_challenge_obj)
        return marathon_obj

    def to_representation(self, instance):
        print(instance)
        # result = super().to_representation(instance)
        # pprint(result)
        marathon_challenges = MarathonChallengeSerializer(instance.marathonchallenge_set.all(), many=True).data
        return {
            'id':                 instance.id,
            'title':              instance.title,
            'is_active':          instance.is_active,
            'description':        instance.description,
            'marathon_challenge': marathon_challenges,
        }

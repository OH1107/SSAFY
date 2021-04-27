from rest_framework import serializers
from .models import Article, Comment


# QuerySet => Serializers => Json response

# List 불러올 때 사용하는 Serializer
class ArticleListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = ('id', 'title', 'created_at')


class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)


# Detail 불러올 때 사용하는 Serializer
class ArticleSerializer(serializers.ModelSerializer):
    # 역참조 필드의 pk 목록에 대한 필드
    # comment_set = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'


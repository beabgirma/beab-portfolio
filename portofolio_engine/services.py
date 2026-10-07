from .models import PerspectiveTranslation, Perspective
from django.db.models import Prefetch,Q


def get_localized_perspective(language_code="en"):
    optimized_query = Perspective.objects.prefetch_related(
        Prefetch(
            'translations',
            queryset=PerspectiveTranslation.objects.filter(
                Q(language=language_code) | Q(language='en')
            ),
            to_attr='prefetched_translations'
        )
    ).order_by('-created_at')
    results = []
    for parent in optimized_query:
        translation_dict={t.language:t for t in parent.prefetched_translations}
        active_translation=translation_dict.get(language_code) or translation_dict.get('en')
        if active_translation:
            results.append({
        'id': parent.id,
        'category': parent.category,
        'created_at': parent.created_at,
        'title': active_translation.title,
        'content': active_translation.content,
        'language': active_translation.language,
            })
        
    return results
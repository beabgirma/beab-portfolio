from django.shortcuts import render
from .models import Project

TRANSLATIONS = {
    'en': {
        'name': 'Beab Girma Yifrashewa',
        'tagline': 'Software Engineer crafting high-performance backend architectures, cloud systems, and web applications.',
        
        'about_tag': 'BIO & JOURNEY 🌍',
        'about_title': 'About & Journey',
        'about_desc': 'Lycée Guébramariam alumnus, Computer Science student at UBCO, and deeply rooted in Ethiopian culture.',
        
        'music_tag': 'SOUND & RHYTHM 🎹',
        'music_title': 'Touches & Rhythm',
        'music_desc': 'Raised by pianist Girma Yifrashewa, music taught me structure and recursion—the exact principles behind clean software design. Inspired by classical piano and production from artists like The Weeknd.',
        
        'projects_tag': 'ENGINEERING 🚀',
        'projects_title': 'Projects',  
        'projects_desc': 'Explore backend architectures, MIS cloud systems, custom databases, and API engineering.',
        
        'skills_tag': 'EXPERIENCE & SKILLS ⚡',
        'skills_title': 'Experiences & Skills',
        'skills_desc': 'African Union Commission MIS intern, selected delegate for China\'s Ministry of Commerce Seminar in Beijing, combined with core backend stacks and trilingual fluency.',
    },
    'fr': {
        'name': 'Beab Girma Yifrashewa',
        'tagline': 'Ingénieur logiciel spécialisé dans les architectures backend haute performance, les systèmes cloud et les applications web.',
        
        'about_tag': 'BIO & PARCOURS 🌍',
        'about_title': 'À Propos & Parcours',
        'about_desc': 'Ancien élève du Lycée Guébramariam, étudiant en informatique à l\'UBCO, et profondément ancré dans la culture éthiopienne.',
        
        'music_tag': 'SON & INSPIRATION 🎹',
        'music_title': 'Touches & Rythmes',
        'music_desc': 'Élevé par le pianiste Girma Yifrashewa, la musique m\'a enseigné la structure et la récursivité—les principes mêmes d\'un code propre. Porté par le piano classique et les productions de The Weeknd.',
        
        'projects_tag': 'INGÉNIERIE 🚀',
        'projects_title': 'Projets',
        'projects_desc': 'Découvrez mes architectures backend, systèmes cloud MIS, bases de données et APIs.',
        
        'skills_tag': 'EXPÉRIENCES & COMPÉTENCES ⚡',
        'skills_title': 'Expériences & Compétences',
        'skills_desc': 'Stagiaire MIS à la Commission de\'l\'Union Africaine, délégué au séminaire du Ministère du Commerce à Pékin, alliés à des compétences techniques et un profil trilingue.',
    },
    'am': {
        'name': 'በአብ ግርማ ይፍራሸዋ',
        'tagline': 'የሶፍትዌር ኢንጂነር፤ ከፍተኛ አፈፃፀም ያላቸውን የኋለኛ ክፍል (Backend) ሲስተሞች፣ የክላውድ መዋቅሮችን እና የዌብ መተግበሪያዎችን የሚገነባ።',
        
        'about_tag': 'ታሪክ እና ጉዞ 🌍',
        'about_title': 'ስለ እኔ እና ጉዞዬ',
        'about_desc': 'የሊሴ ገብረማሪያም ተማሪ የነበርኩ፣ በUBCO የኮምፒውተር ሳይንስ ተማሪ እና ከኢትዮጵያ ባህል ጋር ጠንካራ ቁርኝት ያለው።',
        
        'music_tag': 'ዜማ እና ድምፅ 🎹',
        'music_title': 'ቁልፎች እና ዜማ',
        'music_desc': 'በአባቴ በግርማ ይፍራሸዋ ሙዚቃ አድጌ፣ የሙዚቃ ቅደም-ተከተል ከኮምፒውተር ሳይንስ አልጎሪዝም ጋር ያለውን ግንኙነት ተረድቻለሁ። በፒያኖ ዜማዎች እና በThe Weeknd ስራዎች እነሳሳለሁ።',
        
        'projects_tag': 'ኢንጅነሪንግ 🚀',
        'projects_title': 'ፕሮጀክቶች',
        'projects_desc': 'የኋለኛ ክፍል (Backend) ሲስተሞችን፣ የክላውድ ዳሽቦርዶችን እና APIs ይመልከቱ።',
        
        'skills_tag': 'ልምድ እና ክህሎት ⚡',
        'skills_title': 'የስራ ልምድ እና ክህሎቶች',
        'skills_desc': 'በአፍሪካ ህብረት የMIS ተለማማጅ፣ በቤጂንግ የቻይና ንግድ ሚኒስቴር ሴሚናር ተወካይ፣ ከሶፍትዌር ኢንጂነሪንግ እና የሶስት ቋንቋዎች ችሎታ ጋር።',
    }
}

def get_current_language(request):
    """
    Checks URL query parameter '?lang=' first, falls back to session, then defaults to 'en'.
    Saves language choice in session so navigation keeps state.
    """
    lang = request.GET.get('lang')
    if lang in TRANSLATIONS:
        request.session['lang'] = lang
        return lang
    return request.session.get('lang', 'en')

def home_view(request):
    lang = get_current_language(request)
    return render(request, 'core/index.html', {
        't': TRANSLATIONS[lang],
        'current_lang': lang,
    })

def projects_view(request):
    lang = get_current_language(request)
    projects = Project.objects.all().order_by('-created_at')
    
    return render(request, 'core/projects.html', {
        'projects': projects,
        't': TRANSLATIONS[lang],
        'current_lang': lang,
    })
from django.shortcuts import render
from .models import Chain, Category, Tag

def chain_list(request):
    """
    View to display chains with search and filter functionality
    """
    # Start with all chains
    chains = Chain.objects.all()
    
    # Get filter parameters from GET request
    search_query = request.GET.get('search', '')
    category_id = request.GET.get('category', '')
    tag_ids = request.GET.getlist('tags')
    
    # Apply search filter if provided
    if search_query:
        chains = chains.filter(description__icontains=search_query)
    
    # Apply category filter if provided
    if category_id:
        chains = chains.filter(category_id=category_id)
    
    # Apply tag filters if provided
    if tag_ids:
        for tag_id in tag_ids:
            chains = chains.filter(tags__id=tag_id)
    
    # Get all categories and tags for the filter dropdowns
    categories = Category.objects.all()
    tags = Tag.objects.all()
    
    context = {
        'chains': chains,
        'categories': categories,
        'tags': tags,
        'search_query': search_query,
        'selected_category': category_id,
        'selected_tags': [int(tag_id) for tag_id in tag_ids if tag_id],
    }
    
    return render(request, 'chains/chain_list.html', context)
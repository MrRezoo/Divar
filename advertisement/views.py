from django.shortcuts import render
from django.views.generic import FormView, DetailView, ListView

from advertisement.forms import PostAdvertisementForm
from advertisement.models import Advertisement
from package.models import Package
from .filters import AdvertisementFilter


class PostAdvertisementView(FormView):
    """
    Get form from PostAdvertisementForm
    """

    template_name = "advertisement/post_advertisement.html"
    form_class = PostAdvertisementForm
    success_url = "/"

    def form_valid(self, form):
        """
        Get User from request
        """
        user = self.request.user
        form.cleaned_data["images"] = self.request.FILES.getlist("files")
        form.save(user)
        return super().form_valid(form)


class AdvertisementDetailView(DetailView):
    """
    Get advertisement detail from Advertisement model
    """

    model = Advertisement
    template_name = "advertisement/advertisement_detail.html"

    def get(self, request, *args, **kwargs):
        advertisement = Advertisement.objects.get(pk=kwargs["pk"])
        packages = Package.objects.filter(is_enable=True)
        return render(
            request,
            self.template_name,
            context={"advertisement": advertisement, "packages": packages},
        )


class AdvertisementCityListView(ListView):
    """
    Get advertisement by cities from Advertisement model
    """

    model = Advertisement
    template_name = "advertisement/advertisement_list.html"

    def get_queryset(self):
        city = self.kwargs.get("city")
        queryset = Advertisement.objects.filter(location__city__slug=city)
        filter = AdvertisementFilter(self.request.GET, queryset=queryset)
        return filter.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # parse url to get city
        context["city"] = self.request.path_info.split("/")[3]
        context["filter"] = AdvertisementFilter(
            self.request.GET, queryset=self.get_queryset()
        )
        return context


class AdvertisementCityCategoryListView(ListView):
    """
    Get advertisement by cities and categories from Advertisement model
    """

    model = Advertisement
    template_name = "advertisement/advertisement_list.html"

    def get_queryset(self):
        city = self.kwargs.get("city")
        category = self.kwargs.get("category")
        queryset = Advertisement.objects.filter(
            location__city__slug=city, category__slug=category
        )
        filter = AdvertisementFilter(self.request.GET, queryset=queryset)
        return filter.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # parse url to get city
        context["city"] = self.request.path_info.split("/")[3]
        context["filter"] = AdvertisementFilter(
            self.request.GET, queryset=self.get_queryset()
        )
        return context

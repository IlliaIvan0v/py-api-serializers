from rest_framework.viewsets import ModelViewSet

from cinema.models import Actor, Movie, MovieSession, CinemaHall, Genre
from cinema.serializers import ActorSerializer, MovieSerializer, MovieSessionSerializer, CinemaHallSerializer, \
    GenreSerializer, MovieListSerializer, MovieRetrieveSerializer, MovieSessionListSerializer, \
    MovieSessionRetrieveSerializer


class ActorsViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()


    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieRetrieveSerializer
        return MovieSerializer

    def get_queryset(self):
        if self.action in ("list", "retrieve"):
            return self.queryset.prefetch_related("genres", "actors")
        return Movie.objects.all()


class MovieSessionViewSet(ModelViewSet):
    queryset = MovieSession.objects.all()


    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action == "retrieve":
            return MovieSessionRetrieveSerializer
        return MovieSessionSerializer

    def get_queryset(self):
        if self.action == "list":
            return self.queryset.prefetch_related("movie", "cinema_hall")
        return MovieSession.objects.all()




class CinemaHallViewSet(ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

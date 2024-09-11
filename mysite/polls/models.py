from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)


class Answer(models.Model):
    answer_text = models.CharField(max_length=500)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    answer = models.OneToOneField(Answer, on_delete=models.CASCADE, null=True, blank=True)
    author = models.ManyToManyField(Author, null=True, blank=True)

    # @admin.display(
    #     boolean=True,
    #     ordering="pub_date",
    #     description="Published recently?",
    # )

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
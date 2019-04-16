from django.db import models


class Project(models.Model):
    project_title = models.CharField(max_length=30)
    pub_date = models.DateTimeField('creation date')

    def __str__(self):
        return self.project_title


class Story(models.Model):
    project = models.ForeignKey(Project,
                                on_delete=models.CASCADE)
    story_title = models.CharField(max_length=30)
    user_story = models.TextField()
    acceptance_criteria = models.TextField()
    business_value = models.PositiveIntegerField(default=0)
    estimation = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Story"
        verbose_name_plural = "Stories"

    def __str__(self):
        return self.story_title

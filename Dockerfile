FROM python:latest

WORKDIR /app

COPY . .

# Install Deps
RUN pip install -r requirements.txt

# Install Languages
RUN python -m spacy download da_core_news_sm  # Danish
RUN python -m spacy download nl_core_news_sm  # Dutch
RUN python -m spacy download en_core_web_sm   # English
RUN python -m spacy download fi_core_news_sm  # Finnish
RUN python -m spacy download fr_core_news_sm  # French
RUN python -m spacy download de_core_news_sm  # Ferman
RUN python -m spacy download it_core_news_sm  # Italian
RUN python -m spacy download nb_core_news_sm  # Norwegian
RUN python -m spacy download pt_core_news_sm  # Portuguese
RUN python -m spacy download ro_core_news_sm  # Romanian
RUN python -m spacy download ru_core_news_sm  # Russian
RUN python -m spacy download es_core_news_sm  # Spanish
RUN python -m spacy download sv_core_news_sm  # Swedish

EXPOSE 8080

ENTRYPOINT ["python"]
CMD ["main.py"]

# bloom: hfg-2022
Team Name: oh, JAMN!\
Team Members: Megan Yee (Information Systems), Aloysius Chow (Business Analytics), Natalie Chung (Business), Justin Lim (Commnications and New Media)

### Problem Statement
**NPO:** Daughters of Tomorrow\
**Statement:** How can we get employers to be open and hire women who have less social mobility and may not have access to livelihood opportunities?

### Solution
[Slide Deck](https://docs.google.com/presentation/d/1Fpuio0WL8BtbNvVMoac9N5ahdEWtRjsNWSPDTEnSJXQ/edit?usp=sharing) \
[Prototype](https://hfg2022-xeqmq7fm5a-uc.a.run.app/) \
[Video Demo](https://youtu.be/e9RDUqWFbJ0) \
[Figma](https://www.figma.com/file/KCCUnEaiC6M9Ccg8HVKvr5/DSC-Hackathon-UI%2FUX-Mockup?node-id=0%3A1)


### Credits
https://github.com/kingabzpro/jobzilla_ai/blob/main/jz_skill_patterns.jsonl
For technical skill patterns used for EntityRuler\
https://github.com/nicolamelluso/SkillNER
For soft skill terms patterns used for EntityRuler\
https://github.com/florex/resume_corpus
For resume dataset

### Build instructions
- Clone repository, and download model-best from latest release and extract into base directory
- Build Docker image (port specification in Docker file must be changed depending on service used)
- Google Cloud Run:\
```docker build -t hfg2022```\
```docker tag hfg2022 gcr.io/<GCP PROJECT ID>/hfg2022```\
```docker push gcr.io/<GCP PROJECT ID>/hfg2022```\
```gcloud run deploy ...```


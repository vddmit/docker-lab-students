FROM alpine:3.21

WORKDIR /pro08-entrypoint

COPY app.sh .

RUN chmod +x app.sh

CMD [ "./app.sh" ]
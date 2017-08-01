#!/usr/bin/env python

import webapp2

from google.cloud import storage

client = storage.Client()

bucket = client.get_bucket('<bucket-name>')


class MainHandler(webapp2.RequestHandler):
    def get(self):

        resp = client.list_buckets()
        # just printing all buckets for project
        for b in resp:
            print b
        # or all files in bucket
        for b in bucket.list_blobs():
            print b

        # try to upload data to GCS
        b = bucket.blob('test.txt', chunk_size=262144 * 2)
        b.upload_from_string('tesssssss')

        self.response.write('ok')


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

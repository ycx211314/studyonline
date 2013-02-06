#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.appengine.ext.webapp import util
import webapp2
import study.views as mainHandler
config={}
config['webapp2_extras.sessions'] = {
    'secret_key': 'this is my session key',
    }
app = webapp2.WSGIApplication([
   # (r'/(\w*)',HtmlHandler),
    (r'/',mainHandler.HtmlHandler),
    (r'/(.*)(.html)',mainHandler.HtmlHandler),
    (r"/regist.do",mainHandler.RegistHandler),
    (r"/login.do",mainHandler.LoginHandler),
],config=config, debug=True)
def main():
    util.run_wsgi_app(app)
if __name__ == "__name__":
    main()

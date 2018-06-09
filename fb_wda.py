import wda

c = wda.Client('http://localhost:8100/')

# Show status
print(c.status())

# Press home button
#c.home()

# Hit healthcheck
c.healthcheck()

# Get page source
c.source() # format XML
c.source(accessible=True) # default false, format JSON
#Take screenshot, only can save format png
c.screenshot('screen.png')

with c.session('com.apple.Health') as s:
	print(s.orientation)
#Same as

s = c.session('com.apple.Health')
print(s.orientation)
s.close()

#For web browser like Safari you can define page whit which will be opened:
s = c.session('com.apple.mobilesafari', ['-u', 'https://www.baidu.com/'])
print(s.orientation)
#s.close()
#Session operations
# Current bundleId and sessionId
print(s.bundle_id, s.id)

# One of <PORTRAIT | LANDSCAPE>
print(s.orientation) # expect PORTRAIT

# Change orientation
s.orientation = wda.LANDSCAPE # there are many other directions

# Deactivate App for some time
s.deactivate(5.0) # 5s

# Get width and height
print(s.window_size())
# Expect json output
# For example: {u'height': 736, u'width': 414}

# Simulate touch
s.tap(200, 200)

# Double touch
s.double_tap(200, 200)

# Simulate swipe, utilizing drag api
'''
s.swipe(x1, y1, x2, y2, 0.5) # 0.5s
s.swipe_left()
s.swipe_right()
s.swipe_up()
s.swipe_down()

# tap hold
s.tap_hold(x, y, 1.0)
'''

# Hide keyboard (not working in simulator), did not success using latest WDA
#s.keyboard_dismiss()
#Find element
#Note: if element not found, WDAElementNotFoundError will be raised

# For example, expect: True or False
# using id to find element and check if exists
'''
s(id="URL").exists # return True or False

# using id or other query conditions
s(id='URL')
s(name='URL')
s(text="URL") # text is alias of name
s(nameContains='UR')
s(label='Address')
s(labelContains='Addr')
s(name='URL', index=1) # find the second element. index starts from 0

# combines search conditions
# attributes bellow can combines
# :"className", "name", "label", "visible", "enabled"
s(className='Button', name='URL', visible=True, labelContains="Addr")
#More powerful findding method

s(xpath='//Button[@name="URL"]')
s(classChain='**/Button[`name == "URL"`]')
s(predicate='name LIKE "UR*"')
s('name LIKE "U*L"') # predicate is the first argument, without predicate= is ok
#Element operations (eg: tap, scroll, set_text etc...)
#Exmaple search element and tap
'''
# Get first match Element object
# The function get() is very important.
# when elements founded in 10 seconds(:default:), Element object returns
# or WDAElementNotFoundError raises
e = s(text='新浪新闻').get(timeout=10.0)
# s(text='Dashboard') is Selector
# e is Element object
e.tap() # tap element
#Some times, I just hate to type .get()

#Using python magic tricks to do it again.

# 	using python magic function "__getattr__", it is ok with out type "get()"
s(text='新浪新闻').tap()
# same as
s(text='新浪新闻').get().tap()
#Note: Python magic tricks can not used on get attributes

# Accessing attrbutes, you have to use get()
s(text='新浪新闻').get().value

# Not right
# s(text='Dashboard').value # Bad, always return None
#Click element if exists

s(text='新浪新闻').click_exists() # return immediately if not found
s(text='新浪新闻').click_exists(timeout=5.0) # wait for 5s
#Other Element operations

# Check if elements exists
print(s(text="新浪新闻").exists)

# Find all matches elements, return Array of Element object
s(text='新浪新闻').find_elements()

# Use index to find second element
s(text='新浪新闻')[1].exists

# Use child to search sub elements
s(text='新浪新闻').child(className='Cell').exists

# Default timeout is 10 seconds
# But you can change by
s.set_timeout(10.0)

# do element operations
e.tap()
e.click() # alias of tap
e.clear_text()
e.set_text("Hello world")
e.tap_hold(2.0) # tapAndHold for 2.0s

e.scroll() # scroll to make element visiable

# directions can be "up", "down", "left", "right"
# swipe distance default to its height or width according to the direction
e.scroll('up')

# Set text
e.set_text("Hello WDA") # normal usage
e.set_text("Hello WDA\n") # send text with enter
e.set_text("\b\b\b") # delete 3 chars

# Wait element gone
s(text='Dashboard').wait_gone(timeout=10.0)

# Swipe
s(className="Image").swipe("left")

# Pinch
s(className="Map").pinch(2, 1) # scale=2, speed=1
s(className="Map").pinch(0.1, -1) # scale=0.1, speed=-1 (I donot very understand too)

# properties (bool)
e.accessible
e.displayed
e.enabled

# properties (str)
e.text # ex: Dashboard
e.className # ex: XCUIElementTypeStaticText
e.value # ex: github.com

# Bounds return namedtuple
rect = e.bounds # ex: Rect(x=144, y=28, width=88.0, height=27.0)
rect.x # expect 144
#Alert

print(s.alert.exists)
print(s.alert.text)
s.alert.accept() # Actually do click first alert button
s.alert.dismiss() # Actually do click second alert button
s.alert.wait(5) # if alert apper in 5 second it will return True,else return False (default 20.0)
s.alert.wait() # wait alert apper in 2 second

s.alert.buttons()
# example return: ["设置", "好"]

s.alert.click("设置")
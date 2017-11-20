#center UVA: 38.033779,-78.5080248
#fashion square(north): 38.077046,-78.4750173
# ragged mountain(west): 38.0047972,-78.4849118
# carmax(east): 38.0047972,-78.4849118
# mosby mountain(south): 38.0047972,-78.4849118

from skimage import io


class mapSpider(object):
    def __init__(self, step_width = 0.0015, step_height = 0.0012, center_point = (38.033779,-78.5080248)\
                , style = 'feature:all|element:labels|visibility:off', zoom = '19', size = '600x630'\
                , maptype = ['roadmap', 'satellite'], form = 'jpg'\
                , key = 'AIzaSyCDjxBXc61qrtnc-SzSzI3QhZ8_v-X2mrw', output_dir = './test/'):
        self.step_width = step_width
        self.step_height = step_height
        self.center_point = center_point
        self.style = style
        self.zoom = zoom
        self.size = size
        self.maptype = maptype
        self.form = form
        self.key = key

        self.output_dir = output_dir

    def scrape(self, hor_images, ver_images):
        for i in range(-hor_images / 2, hor_images / 2):
            print('%d images scraped.'%(i*ver_images))
            for j in range(-ver_images / 2, ver_images / 2):
                for t in [0,1]:
                    URL = self.makeURL(self.center_point[0]+i*self.step_width, \
                        self.center_point[1]+j*self.step_height,\
                        self.maptype[t])
                    url_local = self.output_dir + str(t) + '_' + str(i) + '_' + str(j) + '.' + self.form
                    io.imsave(url_local, io.imread(URL))

    def makeURL(self, longi, lati, maptype):
        return 'https://maps.googleapis.com/maps/api/staticmap?' + 'center=' + str(longi)\
                        + ',' + str(lati) + '&style=' + self.style + '&zoom=' + self.zoom \
                        + '&size=' + self.size + '&maptype=' + maptype \
                        + '&format=' + self.form + '&key=' + self.key



if __name__ == "__main__":
    spider = mapSpider()
    spider.scrape(10, 10)
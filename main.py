import pygame

class App:
    #constructor function
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = 640, 400
        self.orange = (255,169,0)
        self.black = (0,0,0)
        

    def on_init(self):
        #initialise all imported pygame modules
        pygame.init()    

        #pygame.display.set_mode(size, flags, depth=0, display=0) returns a Surface.
        #size is a tuple for size of window
        # flags can take various different parameters separated by bitwise 'or' opperator
        # here flags take pygame.HWSURFACE (hardware accelerated, only in fullscreen) and pygame.DOUBLEBUF (recommended for HWSURFACE or OPENGL)
        # if you pass nothing to flags argument it will default to a software driven window   
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

    #on_event() houses code for events such as all key presses, mouse motion etc
    def on_event(self, event):
        #I think the pygame.QUIT event is when you click the Esc cross top right of window. See pygame.quit() below which is different
        if event.type == pygame.QUIT:
            self._running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("K_UP")
            elif event.key == pygame.K_DOWN:
                print("K_DOWN")
            elif event.key == pygame.K_LEFT:
                print("K_LEFT")
            elif event.key == pygame.K_RIGHT:
                print("K_RIGHT")    
        
    #on_loop() houses code for changes to the game world like NPC moves, player moves, AI, gamescore
    def on_loop(self):
        pass


    #on_render() houses code for printing screen graphics   
    def on_render(self):
        
        self._display_surf.fill(self.black)

        for i in range(0, self.width, 10):
            pygame.draw.rect(self._display_surf, self.orange, [i, 0, 10, 10])
            pygame.draw.rect(self._display_surf, self.orange, [i, self.height-10, 10, 10])

        for i in range(0, self.height, 10):
            pygame.draw.rect(self._display_surf, self.orange, [0, i, 10, 10])
            pygame.draw.rect(self._display_surf, self.orange, [self.width-10, i, 10, 10])

        pygame.display.update()
      
        

    def on_cleanup(self):
        #Uninitialize all pygame modules that have previously been initialized. pygame.quit() returns None
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False
        
        while(self._running):
            #pygame.event.get() return a list of events taken from the event queue
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()    


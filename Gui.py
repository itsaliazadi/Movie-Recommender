import tkinter as tk
import Recommendation
import customtkinter as ctk

class Gui(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Movie Recommender")
        self.geometry("600x600")

        ctk.set_default_color_theme("dark-blue")
        ctk.set_appearance_mode("dark")

        self.label = ctk.CTkLabel(self, text="Enter a movie", font=("Times New Roman", 30), width=560, height=40)
        self.label.place(x=43, y=50)

        self.movie_entry = ctk.CTkEntry(self, placeholder_text="Type movie name here", width=560)
        self.movie_entry.place(x=25, y=120)

        self.submit_button = ctk.CTkButton(self, text="Submit", command=self.submit_movie)
        self.submit_button.place(x=250, y=180)

        # Text box for displaying recommendations
        self.recommendation_box = ctk.CTkTextbox(self, width=560, height=300)
        self.recommendation_box.place(x=25, y=220)
        self.recommendation_box.tag_config('green', foreground='Light Green')

        self.suggested_movie = ""
        self.recommendation_box.bind("<Button-1>", self.on_recommendation_click)

    def submit_movie(self):
        movie_title = self.movie_entry.get()
        
        if movie_title:  # Check if the entry is not empty
            recommendations = Recommendation.recommend(movie_title)
            self.display_recommendations(recommendations)

    def display_recommendations(self, recommendations):
        # Clear previous recommendations
        self.recommendation_box.delete("1.0", tk.END)
        

        if type(recommendations) == list:
            for movie in recommendations:
                self.recommendation_box.insert(tk.END, f"-{movie}\n") 
        else:
            self.suggested_movie = recommendations
            # self.recommendation_box.insert(tk.END, f"Sorry!This movie is not available in our database.\nDid you mean '{self.suggested_movie}'?")

            self.recommendation_box.insert(tk.END, "Sorry! This movie is not available in our database.\nDid you mean ")
            self.recommendation_box.insert(tk.END, f"{self.suggested_movie}", 'green')
            self.recommendation_box.insert(tk.END, "?")
             

    def on_recommendation_click(self, event):
        # Check if there is a suggested movie
        if self.suggested_movie:
            self.movie_entry.delete(0, tk.END)  # Clear current entry
            self.movie_entry.insert(0, self.suggested_movie)  # Insert the suggested movie
            self.suggested_movie = None  # Reset the suggestion after use
            self.submit_movie()

if __name__ == "__main__":
    app = Gui()
    app.mainloop()




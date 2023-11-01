using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.AspNetCore.Mvc;
using System.ComponentModel.DataAnnotations;

public class SubmitStoryModel : PageModel
{
    [BindProperty]
    public StoryInputModel StoryInput { get; set; }

    public void OnGet()
    {
        // Initialization code (if any)
    }

    public async Task<IActionResult> OnPostAsync()
    {
        if (!ModelState.IsValid)
        {
            return Page();
        }

        // Process the form data, save to database, etc.
        // Redirect to the story page or another appropriate page
        return RedirectToPage("/Success");
    }
}

public enum GenreType
{
    Fiction,
    NonFiction,
    // Add other genres as needed
}

public class StoryInputModel
{
    [Required]
    public string Title { get; set; }

    [Required]
    public GenreType Genre { get; set; }

    public string Characters { get; set; }

    [Required]
    public string Content { get; set; }
}

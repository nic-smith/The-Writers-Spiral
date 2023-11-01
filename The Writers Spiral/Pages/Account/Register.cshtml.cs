using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using System.Diagnostics;
using System.Threading.Tasks;
using The_Writers_Spiral.Models;

namespace The_Writers_Spiral.Pages.Account
{

    public class RegisterModel : PageModel
    {

        private readonly YourDbContext _context;

        public RegisterModel(YourDbContext context)
        {
            _context = context;
            NewUser = new User();
        }

        [BindProperty]
        public User NewUser { get; set; }

        public void OnGet()
        {
        }

        public async Task<IActionResult> OnPostAsync()
        {
            if (!ModelState.IsValid)
            {
                // Handle validation errors
                return Page();
            }

            _context.User.Add(NewUser);
            var changes = await _context.SaveChangesAsync();  // Here's where SaveChangesAsync is called

            if (changes > 0)
            {
                // Data was saved successfully
                return RedirectToPage("/RegisterConfirmation");
            }
            else
            {
                // Handle the case where no changes were made
                ModelState.AddModelError(string.Empty, "An error occurred while saving. Please try again.");
                return Page();
            }
        }

    }
}

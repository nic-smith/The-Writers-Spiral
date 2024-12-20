using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.AspNetCore.Mvc;
using System.ComponentModel.DataAnnotations;
using System.Threading.Tasks;

namespace The_Writers_Spiral.Pages.Account
{
    public class ResetPasswordModel : PageModel
    {
        [BindProperty]
        public InputModel Input { get; set; }

        public class InputModel
        {
            [Required]
            [EmailAddress]
            public string Email { get; set; }

            [Required]
            public string Token { get; set; }

            [Required]
            [DataType(DataType.Password)]
            public string NewPassword { get; set; }

            [Required]
            [DataType(DataType.Password)]
            [Compare("NewPassword", ErrorMessage = "The passwords do not match.")]
            public string ConfirmPassword { get; set; }
        }

        public void OnGet(string email, string token)
        {
            Input = new InputModel
            {
                Email = email,
                Token = token
            };
        }

        public async Task<IActionResult> OnPostAsync()
        {
            if (!ModelState.IsValid)
            {
                return Page();
            }

            // TODO: Implement password reset logic here
            // You would typically verify the token, ensure the user’s email is correct,
            // and then update the user’s password in the database.

            return RedirectToPage("ResetPasswordConfirmation");
        }
    }
}

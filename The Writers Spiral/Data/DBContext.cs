using Microsoft.EntityFrameworkCore;
using The_Writers_Spiral.Models;

public class YourDbContext : DbContext
{
    public YourDbContext(DbContextOptions<YourDbContext> options)
        : base(options)
    {
    }

    public DbSet<User> User { get; set; }

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        base.OnModelCreating(modelBuilder);

        modelBuilder.Entity<User>(entity =>
        {
            entity.Property(u => u.UserId).HasColumnName("user_id");
            entity.Property(u => u.FirstName).HasColumnName("first_name");
            entity.Property(u => u.LastName).HasColumnName("last_name");
            entity.Property(u => u.Email).HasColumnName("email");
            entity.Property(u => u.Password).HasColumnName("password");
            entity.Property(u => u.UserType).HasColumnName("user_type");
            entity.Property(u => u.PenName).HasColumnName("pen_name");
        });
    }

}

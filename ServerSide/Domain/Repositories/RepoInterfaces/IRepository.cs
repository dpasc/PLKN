using System.Collections.Generic;
using System.Threading.Tasks;

namespace Domain.Repositories.RepoInterfaces{

    public interface IRepository<T> where T : class, IEntity
    {
        Task<List<T>> GetAllRecords();
    }


}
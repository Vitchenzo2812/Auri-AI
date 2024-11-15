import * as S from './styles'

interface Props {
  isSelected: boolean
  brandIcon: JSX.Element
  onClick: () => void
}

const BrandButton = ({ isSelected, brandIcon, onClick }: Props) => {
  const isSelectedBrand = (scale: number) => !isSelected ? { scale } : {}
  
  return (
    <S.Container 
      animate={{ scale: isSelected ? 1.3 : 1 }}
      whileHover={isSelectedBrand(1.1)}
      whileTap={isSelectedBrand(0.9)}
      onClick={onClick}
    >
      {brandIcon}
    </S.Container>
  )
}

export default BrandButton